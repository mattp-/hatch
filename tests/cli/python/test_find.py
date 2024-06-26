def test_not_installed(hatch, helpers):
    name = '3.10'
    result = hatch('python', 'find', name)

    assert result.exit_code == 1, result.output
    assert result.output == helpers.dedent(
        f"""
        Distribution not installed: {name}
        """
    )


def test_binary(hatch, helpers, temp_dir_data, dist_name):
    install_dir = temp_dir_data / 'data' / 'pythons'
    dist = helpers.write_distribution(install_dir, dist_name)

    result = hatch('python', 'find', dist_name)

    assert result.exit_code == 0, result.output
    assert result.output == helpers.dedent(
        f"""
        {dist.python_path}
        """
    )


def test_parent(hatch, helpers, temp_dir_data, dist_name):
    install_dir = temp_dir_data / 'data' / 'pythons'
    dist = helpers.write_distribution(install_dir, dist_name)

    result = hatch('python', 'find', dist_name, '--parent')

    assert result.exit_code == 0, result.output
    assert result.output == helpers.dedent(
        f"""
        {dist.python_path.parent}
        """
    )
