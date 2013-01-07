from __future__ import with_statement

from chef_solo_cup.helpers import sync_cookbooks, sudo_dry
from chef_solo_cup.log import setup_custom_logger


def update(args, config, logger=None):
    if logger is None:
        logger = setup_custom_logger('chef-solo-cup', args)

    sync_cookbooks(args, config, logger=logger)

    sudo_dry("source /etc/profile && `which chef-solo` -c {0}/solo-config.rb -j {0}/dna/{1} -l {2}".format(args.chef_file_dest, config.get('dna_path'), args.loglevel), args, logger=logger)