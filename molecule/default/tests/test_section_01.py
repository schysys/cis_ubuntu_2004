import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_1_1_1_1_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').exists


def test_1_1_1_1_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').is_file


def test_1_1_1_1_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').mode == 0o644


def test_1_1_1_1_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').user == 'root'


def test_1_1_1_1_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.1_cramfs.conf').group == 'root'


def test_1_1_1_2_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').exists


def test_1_1_1_2_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').is_file


def test_1_1_1_2_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').mode == 0o644


def test_1_1_1_2_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').user == 'root'


def test_1_1_1_2_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.2_freevxfs.conf').group == 'root'


def test_1_1_1_3_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.conf').exists


def test_1_1_1_3_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.conf').is_file


def test_1_1_1_3_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.conf').mode == 0o644


def test_1_1_1_3_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.conf').user == 'root'


def test_1_1_1_3_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.3_jffs2.conf').group == 'root'


def test_1_1_1_4_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').exists


def test_1_1_1_4_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').is_file


def test_1_1_1_4_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').mode == 0o644


def test_1_1_1_4_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').user == 'root'


def test_1_1_1_4_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.4_hfs.conf').group == 'root'


def test_1_1_1_5_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.5_hfsplus.conf').exists


def test_1_1_1_5_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.5_hfsplus.conf').is_file


def test_1_1_1_5_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.5_hfsplus.conf').mode == 0o644


def test_1_1_1_5_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.5_hfsplus.conf').user == 'root'


def test_1_1_1_5_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.5_hfsplus.conf').group == 'root'


def test_1_1_1_6_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.6_udf.conf').exists


def test_1_1_1_6_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.6_udf.conf').is_file


def test_1_1_1_6_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.6_udf.conf').mode == 0o644


def test_1_1_1_6_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.6_udf.conf').user == 'root'


def test_1_1_1_6_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.6_udf.conf').group == 'root'


def test_1_1_1_7_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.1.7_vfat.conf').exists


def test_1_1_1_7_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.1.7_vfat.conf').is_file


def test_1_1_1_7_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.1.7_vfat.conf').mode == 0o644


def test_1_1_1_7_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.1.7_vfat.conf').user == 'root'


def test_1_1_1_7_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.1.7_vfat.conf').group == 'root'


def test_1_1_2_tmp_mount_file_exists(host):
    assert host.file('/etc/systemd/system/tmp.mount').exists


def test_1_1_2_tmp_mount_file_isfile(host):
    assert host.file('/etc/systemd/system/tmp.mount').is_file


def test_1_1_2_tmp_mount_file_mode(host):
    assert host.file('/etc/systemd/system/tmp.mount').mode == 0o644


def test_1_1_2_tmp_mount_file_user(host):
    assert host.file('/etc/systemd/system/tmp.mount').user == 'root'


def test_1_1_2_tmp_mount_file_group(host):
    assert host.file('/etc/systemd/system/tmp.mount').group == 'root'


def test_1_1_2_tmp_mount_service_enabled(host):
    assert host.service('tmp.mount').is_enabled


def test_1_1_2_tmp_mount_service_running(host):
    assert host.service('tmp.mount').is_running


def test_1_1_3_tmp_mount_nodev(host):
    assert host.file('/etc/systemd/system/tmp.mount').contains('nodev')


def test_1_1_4_tmp_mount_nosuid(host):
    assert host.file('/etc/systemd/system/tmp.mount').contains('nosuid')


def test_1_1_5_tmp_mount_noexec(host):
    assert host.file('/etc/systemd/system/tmp.mount').contains('noexec')


def test_1_1_6_dev_shm_mount_exists(host):
    assert host.mount_point('/dev/shm').exists


def test_1_1_7_dev_shm_mount_nodev(host):
    assert host.file('/etc/fstab').contains('nodev')


def test_1_1_8_dev_shm_mount_nosuid(host):
    assert host.file('/etc/fstab').contains('nosuid')


def test_1_1_9_dev_shm_mount_noexec(host):
    assert host.file('/etc/fstab').contains('noexec')


def test_1_1_24_file_exists(host):
    assert host.file('/etc/modprobe.d/1.1.24_usb-storage.conf').exists


def test_1_1_24_file_isfile(host):
    assert host.file('/etc/modprobe.d/1.1.24_usb-storage.conf').is_file


def test_1_1_24_file_mode(host):
    assert host.file('/etc/modprobe.d/1.1.24_usb-storage.conf').mode == 0o644


def test_1_1_24_file_user(host):
    assert host.file('/etc/modprobe.d/1.1.24_usb-storage.conf').user == 'root'


def test_1_1_24_file_group(host):
    assert host.file('/etc/modprobe.d/1.1.24_usb-storage.conf').group == 'root'


def test_1_3_1_sudo_package(host):
    assert host.package('sudo').is_installed


def test_1_3_2_sudoers_file_use_pty(host):
    assert host.file('/etc/sudoers').contains('use_pty')


def test_1_3_2_sudoers_file_mode(host):
    assert host.file('/etc/sudoers').mode == 0o640


def test_1_3_3_sudoers_file_logfile(host):
    assert host.file('/etc/sudoers').contains('logfile')


def test_1_3_3_sudoers_file_mode(host):
    assert host.file('/etc/sudoers').mode == 0o640


def test_1_4_1_aide_package(host):
    assert host.package('aide').is_installed


def test_1_4_1_aide_common_package(host):
    assert host.package('aide-common').is_installed


def test_1_4_1_aide_db_file_exists(host):
    assert host.file('/var/lib/aide/aide.db').exists


def test_1_4_1_aide_db_file_isfile(host):
    assert host.file('/var/lib/aide/aide.db').is_file
