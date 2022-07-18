The following is for terminal control information:

about idle 3 sub-network(check if in the correct sub-network):
    ssh -Y pslogin
    ssh -Y psdev
    ssh -Y psbuild-rhel7
    ssh -Y las-console
    source /reg/g/pcds/pyps/conda/py36env.sh
    idle3
    
about Qt designer subnetwork:
    ssh -Y pslogin
    ssh -Y psca
    bash
    source /reg/g/pcds/setup/epicsenv-cur.sh
    source /reg/g/pcds/setup/pcds_shortcuts.sh
    designer
    
about Injection assembled information:
    ssh -Y pslogin
    ssh -Y psbuild-rhel7
    source /reg/g/pcds/setup/epicsenv-cur.sh
    mods_ip1
    mods_crix (for  Harmonic)
    
about Tyler's mirror:
    ssh -Y pslogin
    ssh -Y psdev
    ssh -Y las-console
    ~tjohnson/bin/tile_test_motors.cmd

