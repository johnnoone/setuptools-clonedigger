import subprocess
import setuptools

class ClonediggerCommand(setuptools.Command):

    description = "run clonedigger on all your modules"

    user_options = [
        ('language', 'l', 'the programming language'),
        ('no-recursion', None, 'do not traverse directions recursively'),
        ('output', 'o', 'the name of the output file ("output.html" by \
                        default)'),
        ('clustering-threshold', None, 'read the paper for semantics'),
        ('distance-threshold', None, 'the maximum amount of differences \
                        between pair of sequences in clone pair (5 by \
                        default). Larger value leads to larger amount of \
                        false positives'),
        ('hashing-depth', None, 'default value if 1, read the paper for \
                        semantics. Computation can be speeded up by \
                        increasing this value (but some clones can be \
                        missed)'),
        ('size-threshold', None, 'the minimum clone size. The clone size for \
                        its turn is equal to the count of lines of code in \
                        its the largest fragment'),
        ('clusterize-using-dcup', None, 'mark each statement with its D-cup \
                        value instead of the most similar pattern. This \
                        option together with --hashing-depth=0 make it \
                        possible to catch all considered clones (but it is \
                        slow and applicable only to small programs)'),
        ('dont-print-time', None, 'do not print time'),
        ('force', 'f', ''),
        ('force-diff', None, 'force highlighting of differences based on the \
                        diff algorithm'),
        ('fast', None, 'find only clones, which differ in variable and \
                        function names and constants'),
        ('ignore-dir', None, 'exclude directories from parsing'),
        ('eclipse-output', None, 'for internal usage only'),
        ('cpd-output', None, "output as PMD's CPD's XML format. If output \
                        file not defined, output.xml is generated"),
        ('report-unifiers', None, ''),
        ('func-prefixes', None, 'skip functions/methods with these prefixes \
                        (provide a CSV string as argument)'),
        ('file-list', None, 'a file that contains a list of file names that \
                        must be processed by Clone Digger'),
    ]

    boolean_options = [
        'no-recursion', 'dont-print-time', 'force', 
        'force-diff', 'fast', 'cpd-output', 'report-unifiers'
    ]

    def initialize_options(self):
        for longopt, shortopt, desc in self.user_options:
            setattr(self, longopt.replace('-', '_'), None)

    def finalize_options(self):
        pass

    def run(self):
        options = []
        for longopt, shortopt, desc in self.user_options:
            value = getattr(self, longopt.replace('-', '_'))
            if value == 1 and longopt in self.boolean_options:
                options.append('--{0}'.format(longopt))
            elif value is not None:
                options.append('--{0}={1}'.format(longopt, value))

        subprocess.check_output(['clonedigger'] + options + ["src"])
