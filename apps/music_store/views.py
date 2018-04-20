from django.views.generic import FormView

from apps.music_store.forms import AlbumUploadArchiveForm

from django.core.files.storage import default_storage
from .tasks import get_albums_from_zip
import random


class AlbumUploadArchiveView(FormView):
    """View for uploading archive with albums, which consist from tracks."""
    form_class = AlbumUploadArchiveForm
    template_name = 'music_store/album/upload_archive.html'
    success_url = '/admin/music_store/album/'

    def form_valid(self, form):
        """Override method to actions with a valid form data.

        Concretely, for send a uploaded archive to file handler.
        """
        file = form.files.get('file')
        filepath = default_storage.save(
            name=f'{random.randint(100, 999)}_{random.randint(100, 999)}.zip',
            content=file
        )
        get_albums_from_zip(filepath)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Override method for add `title` in context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Albums Upload'
        return context
