import shutil  # 导入高级文件操作模块
import os  # 导入os模块


def mrfunc(base_name, base_dir, compress, owner='', group='', dry_run=0, logger=None):
    import zipfile  # 导入zipfile模块
    zip_filename = base_name + compress  # 组合压缩文件的名称
    archive_dir = os.path.dirname(base_name)  # 获取压缩文件的目录
    if archive_dir and not os.path.exists(archive_dir):  # 如果指定的路径不存在
        if logger is not None:
            logger.info("creating %s", archive_dir)
        if not dry_run:
            os.makedirs(archive_dir)  # 创建目录
    if logger is not None:  # 如果日志信息不为空
        logger.info("creating '%s' and adding '%s' to it",
                    zip_filename, base_dir)
    if not dry_run:
        # 压缩文件
        with zipfile.ZipFile(zip_filename, "w",
                             compression=zipfile.ZIP_DEFLATED) as zf:
            path = os.path.normpath(base_dir)
            if path != os.curdir:
                zf.write(path, path)
                if logger is not None:
                    logger.info("adding '%s'", path)
            for dirpath, dirnames, filenames in os.walk(base_dir):
                for name in sorted(dirnames):
                    path = os.path.normpath(os.path.join(dirpath, name))
                    zf.write(path, path)
                    if logger is not None:
                        logger.info("adding '%s'", path)
                for name in filenames:
                    path = os.path.normpath(os.path.join(dirpath, name))
                    if os.path.isfile(path):
                        zf.write(path, path)
                        if logger is not None:
                            logger.info("adding '%s'", path)
    return zip_filename  # 返回压缩文件名


shutil.register_unpack_format('mrzip', ['.mrzip'], mrfunc, [('compress', '.mrzip')], '自定义文件格式')
print(shutil.get_unpack_formats())  # 获取支持的解压缩格式
