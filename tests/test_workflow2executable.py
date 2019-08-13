#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `workflow2executable` package."""

import pytest

from click.testing import CliRunner

from workflow2executable import workflow2executable
from workflow2executable import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert 'Missing argument' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output
