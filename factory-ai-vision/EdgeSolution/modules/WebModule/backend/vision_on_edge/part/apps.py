"""
Parts App
"""
import logging
import sys

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class PartsConfig(AppConfig):
    """
    Parts App Config
    """
    name = 'vision_on_edge.part'

    def ready(self):
        """
        Part App ready
        """
        if 'runserver' in sys.argv:
            # Import models in migrate/makemigration will occurs error.
            # pylint: disable = import-outside-toplevel
            # pylint: disable = unused-import

            from vision_on_edge.part.models import Part
            from .signals import azure_setting_change_handler

            logger.info("Part App Config ready while running server")

            create_demo = True
            if create_demo:
                logger.info("Creating demo parts...")
                # for partname in ['Box', 'Barrel', 'Hammer',
                #   'Screwdriver', 'Bottle', 'Plastic bag']:
                for partname in [
                        'aeroplane',
                        'bicycle',
                        'bird',
                        'boat',
                        'bottle',
                        'bus',
                        'car',
                        'cat',
                        'chair',
                        'cow',
                        'diningtable',
                        'dog',
                        'horse',
                        'motorbike',
                        'person',
                        'pottedplant',
                        'sheep',
                        'sofa',
                        'train',
                        'tvmonitor',
                ]:
                    Part.objects.update_or_create(
                        name=partname,
                        is_demo=True,
                        defaults={'description': "Demo"})
                logger.info("Creating demo parts finished.")

            logger.info("Part App Config end while running server")
