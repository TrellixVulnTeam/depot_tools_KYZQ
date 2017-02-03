# pylint: disable=no-member,E1103
# pylint: disable=protected-access
  """Sets up and tears down the mocks but doesn't test anything as-is."""
  if input_api.change.ERROR:
  if input_api.change.PROMPT_WARNING:
diff --git %(filename)s %(filename)s
index fe3de7b..54ae6e1 100755
--- %(filename)s       2011-02-09 10:38:16.517224845 -0800
+++ %(filename)s       2011-02-09 10:38:53.177226516 -0800
      'auth', 'cPickle', 'cpplint', 'cStringIO',
      presubmit.os.path.join('foo', 'haspresubmit', 'yodle', 'smart.h'),
      presubmit.os.path.join('moo', 'mat', 'gat', 'yo.h'),
      presubmit.os.path.join('foo', 'luck.h'),
    presubmit.os.path.isfile(presubmit.os.path.join(self.fake_root_dir,
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'foo')).AndReturn([])
    presubmit.os.listdir(presubmit.os.path.join(self.fake_root_dir, 'foo',
        presubmit.os.path.join(self.fake_root_dir, 'foo', 'haspresubmit',
        presubmit.os.path.join(
            self.fake_root_dir, 'foo', 'haspresubmit', 'yodle')).AndReturn(
        presubmit.os.path.join(
            self.fake_root_dir, 'foo', 'haspresubmit', 'yodle',
            'PRESUBMIT.py')).AndReturn(True)
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'moo')).AndReturn([])
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'moo', 'mat')).AndReturn([])
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'moo', 'mat', 'gat')).AndReturn([])
          presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py'),
          presubmit.os.path.join(
              self.fake_root_dir, 'foo', 'haspresubmit', 'PRESUBMIT.py'),
          presubmit.os.path.join(
              self.fake_root_dir, 'foo', 'haspresubmit', 'yodle',
              'PRESUBMIT.py')
    presubmit.os.path.isfile(presubmit.os.path.join(self.fake_root_dir,
    presubmit.os.path.isfile(presubmit.os.path.join(self.fake_root_dir,
    presubmit.os.path.isfile(presubmit.os.path.join(self.fake_root_dir,
        presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py'),
        presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT-user.py'),
    root_dir = presubmit.os.path.join(sys_root_dir, 'foo', 'bar')
      presubmit.os.path.join('moo', 'test2.cc'),
      presubmit.os.path.join('zoo', 'test3.cc')
    presubmit.os.listdir(presubmit.os.path.join(
        sys_root_dir, 'foo')).AndReturn(['PRESUBMIT.py'])
    presubmit.os.path.isfile(presubmit.os.path.join(
        sys_root_dir, 'foo', 'PRESUBMIT.py')).AndReturn(True)
    presubmit.os.listdir(presubmit.os.path.join(
        sys_root_dir, 'foo', 'bar')).AndReturn([])
    presubmit.os.listdir(presubmit.os.path.join(
        sys_root_dir, 'foo', 'bar', 'moo')).AndReturn(['PRESUBMIT.py'])
    presubmit.os.path.isfile(presubmit.os.path.join(
        sys_root_dir, 'foo', 'bar', 'moo', 'PRESUBMIT.py')).AndReturn(True)
    presubmit.os.listdir(presubmit.os.path.join(
        sys_root_dir, 'foo', 'bar', 'zoo')).AndReturn([])
          presubmit.os.path.join(sys_root_dir, 'foo', 'PRESUBMIT.py'),
          presubmit.os.path.join(
              sys_root_dir, 'foo', 'bar', 'moo', 'PRESUBMIT.py')
      if not op.startswith('D'):
    self.failUnless(len(change.AffectedFiles()) == 7)
    self.failUnless(len(change.AffectedFiles(include_deletes=False)) == 5)
    affected_text_files = change.AffectedTestableFiles()
      presubmit.GitChange(
       '  if not input_api.change.ERROR:\n'
  def testDoPresubmitChecksNoWarningsOrErrors(self):
    haspresubmit_path = presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit', 'PRESUBMIT.py')
    root_path = presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py')
    inherit_path = presubmit.os.path.join(
        self.fake_root_dir, self._INHERIT_SETTINGS)
    presubmit.gclient_utils.FileRead(root_path, 'rU').AndReturn(
        self.presubmit_text)
    presubmit.gclient_utils.FileRead(haspresubmit_path, 'rU').AndReturn(
        self.presubmit_text)
    # Make a change which will have no warnings.
    change = self.ExampleChange(extra_lines=['STORY=http://tracker/123'])

        change=change, committing=False, verbose=True,
        output_stream=None, input_stream=None,
        default_presubmit=None, may_prompt=False, rietveld_obj=None)
    self.failUnless(output.should_continue())
    self.assertEqual(output.getvalue().count('!!'), 0)
    self.assertEqual(output.getvalue().count('??'), 0)
    presubmit_path = presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py')
    haspresubmit_path = presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit', 'PRESUBMIT.py')
    inherit_path = presubmit.os.path.join(
        self.fake_root_dir, self._INHERIT_SETTINGS)
      presubmit.os.listdir(presubmit.os.path.join(
          self.fake_root_dir, 'haspresubmit')).AndReturn(['PRESUBMIT.py'])
      presubmit.gclient_utils.FileRead(presubmit_path, 'rU').AndReturn(
          self.presubmit_text)
      presubmit.gclient_utils.FileRead(haspresubmit_path, 'rU').AndReturn(
          self.presubmit_text)
    # Make a change with a single warning.
    change = self.ExampleChange(extra_lines=['PROMPT_WARNING=yes'])

        change=change, committing=False, verbose=True,
        output_stream=None, input_stream=input_buf,
        default_presubmit=None, may_prompt=True, rietveld_obj=None)
        change=change, committing=False, verbose=True,
        output_stream=None, input_stream=input_buf,
        default_presubmit=None, may_prompt=True, rietveld_obj=None)
  def testDoPresubmitChecksWithWarningsAndNoPrompt(self):
    presubmit_path = presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py')
    haspresubmit_path = presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit', 'PRESUBMIT.py')
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit')).AndReturn(['PRESUBMIT.py'])
    presubmit.os.path.isfile(haspresubmit_path).AndReturn(True)
    presubmit.gclient_utils.FileRead(presubmit_path, 'rU').AndReturn(
        self.presubmit_text)
    presubmit.gclient_utils.FileRead(haspresubmit_path, 'rU').AndReturn(
        self.presubmit_text)
    presubmit.random.randint(0, 4).AndReturn(1)
    self.mox.ReplayAll()

    change = self.ExampleChange(extra_lines=['PROMPT_WARNING=yes'])

    # There is no input buffer and may_prompt is set to False.
    output = presubmit.DoPresubmitChecks(
        change=change, committing=False, verbose=True,
        output_stream=None, input_stream=None,
        default_presubmit=None, may_prompt=False, rietveld_obj=None)
    # A warning is printed, and should_continue is True.
    self.failUnless(output.should_continue())
    self.assertEquals(output.getvalue().count('??'), 2)
    self.assertEqual(output.getvalue().count('(y/N)'), 0)
    self.assertEqual(output.getvalue().count(
        'Running presubmit upload checks ...\n'), 1)

  def testDoPresubmitChecksNoWarningPromptIfErrors(self):
    presubmit_path = presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py')
    haspresubmit_path = presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit', 'PRESUBMIT.py')
    inherit_path = presubmit.os.path.join(
        self.fake_root_dir, self._INHERIT_SETTINGS)
    presubmit.os.path.isfile(inherit_path).AndReturn(False)
    presubmit.os.listdir(self.fake_root_dir).AndReturn(['PRESUBMIT.py'])
    presubmit.os.path.isfile(presubmit_path).AndReturn(True)
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit')).AndReturn(['PRESUBMIT.py'])
    change = self.ExampleChange(extra_lines=['ERROR=yes'])
    output = presubmit.DoPresubmitChecks(
        change=change, committing=False, verbose=True,
        output_stream=None, input_stream=None,
        default_presubmit=None, may_prompt=True, rietveld_obj=None)
    self.failIf(output.should_continue())
    self.assertEqual(output.getvalue().count('??'), 0)
    self.assertEqual(output.getvalue().count('!!'), 2)
    always_fail_presubmit_script = """
    inherit_path = presubmit.os.path.join(
        self.fake_root_dir, self._INHERIT_SETTINGS)
    presubmit.os.listdir(self.fake_root_dir).AndReturn([])
    presubmit.os.listdir(presubmit.os.path.join(
        self.fake_root_dir, 'haspresubmit')).AndReturn(['PRESUBMIT.py'])
    presubmit.os.path.isfile(presubmit.os.path.join(self.fake_root_dir,

    change = self.ExampleChange(extra_lines=['STORY=http://tracker/123'])
        change=change, committing=False, verbose=True,
        output_stream=None, input_stream=input_buf,
        default_presubmit=always_fail_presubmit_script,
        may_prompt=False, rietveld_obj=None)
  def testDoPresubmitChecksWithTags(self):
    tag_checker_presubmit_script = """
    inherit_path = presubmit.os.path.join(
        self.fake_root_dir, self._INHERIT_SETTINGS)
    output_buf = StringIO.StringIO()
    presubmit_output = presubmit.DoPresubmitChecks(
        change=change, committing=False, verbose=True,
        output_stream=output_buf, input_stream=input_buf,
        default_presubmit=tag_checker_presubmit_script,
        may_prompt=False, rietveld_obj=None)

    self.failUnless(presubmit_output)
    self.assertEquals(output_buf.getvalue(),
    change = self.ExampleChange(
        extra_lines=['STORY=http://tracker.com/42', 'BUG=boo\n'])
  def ExampleChange(self, extra_lines=None):
    """Returns an example Change instance for tests."""
    description_lines = [
      'Hello there',
      'This is a change',
    ] + (extra_lines or [])
    files = [
      ['A', presubmit.os.path.join('haspresubmit', 'blat.cc')],
    ]
    return presubmit.Change(
        name='mychange',
        description='\n'.join(description_lines),
        local_root=self.fake_root_dir,
        files=files,
        issue=0,
        patchset=0,
        author=None)

    filename_linux = presubmit.os.path.join('linux_only', 'penguin.cc')
    root_presubmit = presubmit.os.path.join(self.fake_root_dir, 'PRESUBMIT.py')
    linux_presubmit = presubmit.os.path.join(
        self.fake_root_dir, 'linux_only', 'PRESUBMIT.py')
    inherit_path = presubmit.os.path.join(
        self.fake_root_dir, self._INHERIT_SETTINGS)
    listdir(presubmit.os.path.join(
        self.fake_root_dir, 'linux_only')).AndReturn(['PRESUBMIT.py'])
        'AffectedTestableFiles',
      ['A', presubmit.os.path.join('foo', 'blat.cc'), True],
      ['M', presubmit.os.path.join('foo', 'blat', 'READ_ME2'), True],
      ['M', presubmit.os.path.join('foo', 'blat', 'binary.dll'), True],
      ['M', presubmit.os.path.join('foo', 'blat', 'weird.xyz'), True],
      ['M', presubmit.os.path.join('foo', 'blat', 'another.h'), True],
      ['M', presubmit.os.path.join('foo', 'third_party', 'third.cc'), True],
      ['D', presubmit.os.path.join('foo', 'mat', 'beingdeleted.txt'), False],
      ['M', presubmit.os.path.join('flop', 'notfound.txt'), False],
      ['A', presubmit.os.path.join('boo', 'flap.h'), True],
    diffs = []
    for _, f, exists in files:
      full_file = presubmit.os.path.join(self.fake_root_dir, f)
      if exists and f.startswith('foo/'):
        presubmit.os.path.isfile(full_file).AndReturn(exists)
      diffs.append(self.presubmit_diffs % {'filename': f})
    presubmit.scm.GIT.GenerateDiff(
        self.fake_root_dir, branch=None, files=[], full_move=True
        ).AndReturn('\n'.join(diffs))
    change = presubmit.GitChange(
        [[f[0], f[1]] for f in files],
        presubmit.os.path.join(self.fake_root_dir, 'foo', 'PRESUBMIT.py'),
      presubmit.os.path.isfile(full_item).AndReturn(True)
    change = presubmit.GitChange(
      presubmit.os.path.isfile(full_item).AndReturn(True)
    change = presubmit.GitChange(
      ['A', presubmit.os.path.join('isdir', 'blat.cc')],
      ['M', presubmit.os.path.join('elsewhere', 'ouf.cc')],
    affected_files = change.AffectedFiles()
    self.assertEquals(
        affected_files[0].AbsoluteLocalPath(),
        presubmit.normpath(presubmit.os.path.join(self.fake_root_dir, 'isdir')))
    self.assertEquals(
        affected_files[1].AbsoluteLocalPath(),
        presubmit.normpath(presubmit.os.path.join(
            self.fake_root_dir, 'isdir/blat.cc')))
    paths_from_change = change.AbsoluteLocalPaths()
    presubmit_path = presubmit.os.path.join(
        self.fake_root_dir, 'isdir', 'PRESUBMIT.py')
    paths_from_api = api.AbsoluteLocalPaths()
      self.assertEqual(
          absolute_paths[0],
          presubmit.normpath(presubmit.os.path.join(
              self.fake_root_dir, 'isdir')))
      self.assertEqual(
          absolute_paths[1],
          presubmit.normpath(presubmit.os.path.join(
              self.fake_root_dir, 'isdir', 'blat.cc')))
    api.AffectedTestableFiles(include_deletes=False)
      'GenerateScmDiff', 'IsTestableFile', 'IsTextFile', 'LocalPath',
      'NewContents',
    af = presubmit.GitAffectedFile('foo/blat.cc', 'M', self.fake_root_dir, None)
  def testIsTestableFile(self):
        presubmit.GitAffectedFile('foo/blat.txt', 'M', self.fake_root_dir,
        presubmit.GitAffectedFile('foo/binary.blob', 'M', self.fake_root_dir,
        presubmit.GitAffectedFile('blat/flop.txt', 'D', self.fake_root_dir,
    presubmit.os.path.isfile(f_blat).AndReturn(True)
    presubmit.os.path.isfile(f_blob).AndReturn(True)
    output = filter(lambda x: x.IsTestableFile(), files)
    self.assertEquals(2, len(output))
        'AbsoluteLocalPaths', 'AffectedFiles', 'AffectedTestableFiles',
        'AffectedTextFiles',
        'AllFiles', 'DescriptionText', 'FullDescriptionText', 'LocalPaths',
        'Name', 'RepositoryRoot', 'RightHandSideLines',
    self.assertEquals(1, len(change.AffectedFiles()))
    self.assertEquals('Y', change.AffectedFiles()[0].Action())
    # pylint: disable=no-self-use
      'CheckAuthorizedAuthor',
    affected_file = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file1 = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file2 = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file1 = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file2 = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file3 = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file4 = self.mox.CreateMock(presubmit.GitAffectedFile)
    def test(include_deletes=True, file_filter=None):
    change = self.mox.CreateMock(presubmit.GitChange)
    affected_file = self.mox.CreateMock(presubmit.GitAffectedFile)
    affected_file = self.mox.CreateMock(presubmit.GitAffectedFile)
      affected_file.LocalPath().AndReturn('foo/xyz.cc')
      change.AffectedFiles(file_filter=None).AndReturn([affected_file])
      if issue:
        if rietveld_response:
          input_api.rietveld.get_issue_properties(
              issue=int(input_api.change.issue), messages=True).AndReturn(
                  rietveld_response)
        elif gerrit_response:
          input_api.gerrit._FetchChangeDetail = lambda _: gerrit_response

      people.add(change.author_email)
      fake_db.files_not_covered_by(set(['foo/xyz.cc']),
          people).AndReturn(uncovered_files)
      if not is_committing and uncovered_files:
        fake_db.reviewers_for(set(['foo']),
            change.author_email).AndReturn(change.author_email)
        expected_output='This is a dry run, but these failures would be ' +
                        'reported on commit:\nMissing LGTM from someone ' +
                        'other than john@example.com\n')
    affected_file = self.mox.CreateMock(presubmit.GitAffectedFile)