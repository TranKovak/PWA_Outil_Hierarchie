# -*- coding: utf-8 -*-
from loguru import logger
from grhtools.xlsx import get_borders, get_alignment, get_column_letter, get_patternfill, get_font
from grhtools.xlsx import set_alignment, set_print_settings, set_error_colors, set_success_colors, set_warning_colors
from grhtools.config import Config
from grhtools.pegase import get_import_masks

if __name__ == '__main__':
    from loguru import logger
    from random import randint

    c = Config('test_project')
    logger.debug(c)
    c.rubriques['170104'] = randint(0, 10000)
    c.save_config('test_project')
    d = Config('test_project')
    logger.debug(d.rubriques)
