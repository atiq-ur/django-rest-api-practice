from rest_framework import renderers
import json

class JSONRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Check if the response has a status_code and it indicates an error
        response = renderer_context.get('response', None)
        if response is not None and response.status_code >= 400:
            # Wrap errors
            data = {'errors': data}

        return super().render(data, accepted_media_type, renderer_context)
