try:
    from subprocess import check_output
except ImportError:
    # pre2.7 compatibility
    from subprocess import Popen, CalledProcessError
    def check_output(args):
        try:
            return Popen(args).communicate()[0]
        except OSError as e:
            raise CalledProcessError(*e)

import setuptools
from distutils.errors import DistutilsSetupError

class ClonediggerCommand(setuptools.Command):

    description = "run clonedigger on all your modules"

    user_options = [
        ('clonedigger-file=', None, 'Output file.must be html or xml '
                        '("clonedigger-output.html" by default)'),
        ('clonedigger-language=', None, 'the programming language'),
        ('clonedigger-no-recursion', None, 'do not traverse directions '
                        'recursively'),
        ('clonedigger-clustering-threshold=', None, 'read the paper for '
                        'semantics'),
        ('clonedigger-distance-threshold=', None, 'the maximum amount of '
                        'differences between pair of sequences in clone pair '
                        '(5 by default). Larger value leads to larger amount '
                        'of false positives'),
        ('clonedigger-hashing-depth=', None, 'default value if 1, read the '
                        'paper for semantics. Computation can be speeded up '
                        'by increasing this value (but some clones can be '
                        'missed)'),
        ('clonedigger-size-threshold=', None, 'the minimum clone size. The '
                        'clone size for its turn is equal to the count of '
                        'lines of code in its the largest fragment'),
        ('clonedigger-clusterize-using-dcup=', None, 'mark each statement '
                        'with its D-cup value instead of the most similar '
                        'pattern. This option together with '
                        '--clonedigger-hashing-depth=0 make it  possible to '
                        'catch all considered clones (but it is slow and '
                        'applicable only to small programs)'),
        ('clonedigger-dont-print-time', None, 'do not print time'),
        ('clonedigger-force', None, ''),
        ('clonedigger-force-diff', None, 'force highlighting of differences '
                        'based on the diff algorithm'),
        ('clonedigger-fast', None, 'find only clones, which differ in '
                        'variable and function names and constants'),
        ('clonedigger-ignore-dir=', None, 'exclude directories from parsing'),
        ('clonedigger-eclipse-output=', None, 'for internal usage only'),
        ('clonedigger-report-unifiers', None, ''),
        ('clonedigger-func-prefixes=', None, 'skip functions/methods with these '
                        'prefixes (provide a CSV string as argument)'),
        ('clonedigger-file-list=', None, 'a file that contains a list of file '
                        'names that must be processed by Clone Digger'),
    ]

    boolean_options = [
        'clonedigger-no-recursion', 'clonedigger-dont-print-time',
        'clonedigger-force', 'clonedigger-force-diff', 'clonedigger-fast',
        'clonedigger-report-unifiers'
    ]

    def initialize_options(self):
        for longopt, shortopt, desc in self.user_options:
            setattr(self, longopt.replace('-', '_'), None)
        self.clonedigger_file = 'clonedigger-output.html'
        self.cpd_output = False
        self.clonedigger_language = None
        self.clonedigger_clustering_threshold = None
        self.clonedigger_distance_threshold = None
        self.clonedigger_hashing_depth = None
        self.clonedigger_size_threshold = None
        self.clonedigger_clusterize_using_dcup = None
        self.clonedigger_ignore_dir = None
        self.clonedigger_eclipse_output = None
        self.clonedigger_func_prefixes = None
        self.clonedigger_file_list = None

    def finalize_options(self):
        ext = self.clonedigger_file.rsplit('.', 1)[-1]
        if ext not in ('html', 'xml'):
            raise DistutilsSetupError('clonedigger-file must an " \
                    "xml or html file')

        if ext == 'xml':
            self.cpd_output = True

    def run(self):
        options = []
        for longopt, shortopt, desc in self.user_options:
            if longopt == 'clonedigger-file=':
                if self.cpd_output:
                    options.append('--cpd-output')
                options.append('--output={0}'.format(self.clonedigger_file))
                continue

            value = getattr(self, longopt.replace('-', '_').rstrip('='))
            realopt = longopt.lstrip('clonedigger-').rstrip('=')
            if value == 1 and longopt in self.boolean_options:
                options.append('--{0}'.format(realopt))
            elif value is not None:
                options.append('--{0}={1}'.format(realopt, value))

        check_output(['clonedigger'] + options + ["src"])
