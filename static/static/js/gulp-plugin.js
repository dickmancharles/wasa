Skip to content
 

Search…
All gists
GitHub
New gist
@dickmancharles
  Star 139
  Fork 25
  @mlouromlouro/gulpfile.js
Last active a day ago
Embed  
<script src="https://gist.github.com/mlouro/8886076.js"></script>
  Download ZIP
 Code  Revisions 7  Stars 139  Forks 25
gulpfile.js with browserify, jshint, libsass, browserSync for livereload, image optimization and system notifications on errors
Raw  gulpfile.js
'use strict';
var gulp = require('gulp');
var gutil = require('gulp-util');
var del = require('del');
var uglify = require('gulp-uglify');
var gulpif = require('gulp-if');
var exec = require('child_process').exec;


var notify = require('gulp-notify');

var buffer = require('vinyl-buffer');
var argv = require('yargs').argv;
// sass
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer-core');
var sourcemaps = require('gulp-sourcemaps');
// BrowserSync
var browserSync = require('browser-sync');
// js
var watchify = require('watchify');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
// image optimization
var imagemin = require('gulp-imagemin');
// linting
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
// testing/mocha
var mocha = require('gulp-mocha');

// gulp build --production
var production = !!argv.production;
// determine if we're doing a build
// and if so, bypass the livereload
var build = argv._.length ? argv._[0] === 'build' : false;
var watch = argv._.length ? argv._[0] === 'watch' : true;

// ----------------------------
// Error notification methods
// ----------------------------
var beep = function() {
  var os = require('os');
  var file = 'gulp/error.wav';
  if (os.platform() === 'linux') {
    // linux
    exec("aplay " + file);
  } else {
    // mac
    console.log("afplay " + file);
    exec("afplay " + file);
  }
};
var handleError = function(task) {
  return function(err) {
    beep();
    
      notify.onError({
        message: task + ' failed, check the logs..',
        sound: false
      })(err);
    
    gutil.log(gutil.colors.bgRed(task + ' error:'), gutil.colors.red(err));
  };
};
// --------------------------
// CUSTOM TASK METHODS
// --------------------------
var tasks = {
  // --------------------------
  // Delete build folder
  // --------------------------
  clean: function(cb) {
    del(['build/'], cb);
  },
  // --------------------------
  // Copy static assets
  // --------------------------
  assets: function() {
    return gulp.src('./client/assets/**/*')
      .pipe(gulp.dest('build/assets/'));
  },
  // --------------------------
  // HTML
  // --------------------------
  // html templates (when using the connect server)
  templates: function() {
    gulp.src('templates/*.html')
      .pipe(gulp.dest('build/'));
  },
  // --------------------------
  // SASS (libsass)
  // --------------------------
  sass: function() {
    return gulp.src('./client/scss/*.scss')
      // sourcemaps + sass + error handling
      .pipe(gulpif(!production, sourcemaps.init()))
      .pipe(sass({
        sourceComments: !production,
        outputStyle: production ? 'compressed' : 'nested'
      }))
      .on('error', handleError('SASS'))
      // generate .maps
      .pipe(gulpif(!production, sourcemaps.write({
        'includeContent': false,
        'sourceRoot': '.'
      })))
      // autoprefixer
      .pipe(gulpif(!production, sourcemaps.init({
        'loadMaps': true
      })))
      .pipe(postcss([autoprefixer({browsers: ['last 2 versions']})]))
      // we don't serve the source files
      // so include scss content inside the sourcemaps
      .pipe(sourcemaps.write({
        'includeContent': true
      }))
      // write sourcemaps to a specific directory
      // give it a file and save
      .pipe(gulp.dest('build/css'));
  },
  // --------------------------
  // Browserify
  // --------------------------
  browserify: function() {
    var bundler = browserify('./client/js/index.js', {
      debug: !production,
      cache: {}
    });
    // determine if we're doing a build
    // and if so, bypass the livereload
    var build = argv._.length ? argv._[0] === 'build' : false;
    if (watch) {
      bundler = watchify(bundler);
    }
    var rebundle = function() {
      return bundler.bundle()
        .on('error', handleError('Browserify'))
        .pipe(source('build.js'))
        .pipe(gulpif(production, buffer()))
        .pipe(gulpif(production, uglify()))
        .pipe(gulp.dest('build/js/'));
    };
    bundler.on('update', rebundle);
    return rebundle();
  },
  // --------------------------
  // linting
  // --------------------------
  lintjs: function() {
    return gulp.src([
        'gulpfile.js',
        './client/js/index.js',
        './client/js/**/*.js'
      ]).pipe(jshint())
      .pipe(jshint.reporter(stylish))
      .on('error', function() {
        beep();
      });
  },
  // --------------------------
  // Optimize asset images
  // --------------------------
  optimize: function() {
    return gulp.src('./client/assets/**/*.{gif,jpg,png,svg}')
      .pipe(imagemin({
        progressive: true,
        svgoPlugins: [{removeViewBox: false}],
        // png optimization
        optimizationLevel: production ? 3 : 1
      }))
      .pipe(gulp.dest('./client/assets/'));
  },
  // --------------------------
  // Testing with mocha
  // --------------------------
  test: function() {
    return gulp.src('./client/**/*test.js', {read: false})
      .pipe(mocha({
        'ui': 'bdd',
        'reporter': 'spec'
      })
    );
  },


};

gulp.task('browser-sync', function() {
    browserSync({
        server: {
            baseDir: "./build"
        },
        port: process.env.PORT || 3000
    });
});

gulp.task('reload-sass', ['sass'], function(){
  browserSync.reload();
});
gulp.task('reload-js', ['browserify'], function(){
  browserSync.reload();
});
gulp.task('reload-templates', ['templates'], function(){
  browserSync.reload();
});

// --------------------------
// CUSTOMS TASKS
// --------------------------
gulp.task('clean', tasks.clean);
// for production we require the clean method on every individual task
var req = build ? ['clean'] : [];
// individual tasks
gulp.task('templates', req, tasks.templates);
gulp.task('assets', req, tasks.assets);
gulp.task('sass', req, tasks.sass);
gulp.task('browserify', req, tasks.browserify);
gulp.task('lint:js', tasks.lintjs);
gulp.task('optimize', tasks.optimize);
gulp.task('test', tasks.test);

// --------------------------
// DEV/WATCH TASK
// --------------------------
gulp.task('watch', ['assets', 'templates', 'sass', 'browserify', 'browser-sync'], function() {

  // --------------------------
  // watch:sass
  // --------------------------
  gulp.watch('./client/scss/**/*.scss', ['reload-sass']);

  // --------------------------
  // watch:js
  // --------------------------
  gulp.watch('./client/js/**/*.js', ['lint:js', 'reload-js']);

  // --------------------------
  // watch:html
  // --------------------------
  gulp.watch('./templates/**/*.html', ['reload-templates']);

  gutil.log(gutil.colors.bgGreen('Watching for changes...'));
});

// build task
gulp.task('build', [
  'clean',
  'templates',
  'assets',
  'sass',
  'browserify'
]);

gulp.task('default', ['watch']);

// gulp (watch) : for development and livereload
// gulp build : for a one off development build
// gulp build --production : for a minified production build
 @alexbw
alexbw commented on Feb 22
Fantastic! You mentioned in a recent blog post that you access your site locally via port 8000. How are you configuring this proxy, and are you doing it in Vagrant?
@jterskine
jterskine commented on Mar 4
+1
@roganov
roganov commented on Mar 15
How do you deal with third-party styles and scripts (such as Twitter Bootstrap)? Do you put these files under client directory?
@mlouro
Owner
mlouro commented on Jul 9
@roganov, the third-party styles go into client/assets and get copied over to the build directory.

@alexbw, the proxy is setup via browserSync's options, it's not in this gist, see https://github.com/lincolnloop/generator-frigate/blob/master/app/templates/_gulp.config.js#L44-L46. When proxyOptions.proxy is set, browserSync will just forward requests it can't handle over to the address you define there.
@steppo40
steppo40 commented on Sep 11
+1
@deepflame
deepflame commented on Sep 18
nicely structured, well done. Thanks for sharing!
@Dovizu
Dovizu commented on Sep 26
I had to comment out var req = build ? ['clean'] : []; and replace it with var req = []; on line 221, because for some reason gulp build would stop right after clean.

$ gulp build
autoprefixer-core was deprecated. Use autoprefixer package.
[01:17:14] Using gulpfile /code/gulpfile.js
[01:17:14] Starting 'clean'...
If anyone knows why or has a better fix, please help!
@marlomgirardi
marlomgirardi commented on Sep 27
Hey! child_process isn't recommended.

New implementation:

//...
let exec = require('gulp-exec');
let autoprefixer = require('gulp-autoprefixer'); // old autoprefixer-core
//...

let beep = function() {
    let os = require('os');
    let error = gulp.src('path/error.wav');
    if (os.platform() === 'linux') {
        error.pipe(exec('aplay <%= file.path %>'));
    } else {
        // mac
        error.pipe(exec('afplay <%= file.path %>'));
    }
};

//...
@rafaelvasco
rafaelvasco commented on Sep 29
Many thanks for this ! Using it for everything now :D
@petulla
petulla commented on Oct 25
Thanks for this. Did you make the package.json available?
@kevinkucharczyk
kevinkucharczyk commented on Nov 5
I ran into the same problem as @Dovizu. Apparently new versions of del have changed in how they handle the callback. Here's an improved clean task which will run properly:

clean: function(callback) {
  del(['build/']).then(function() {
    callback();
  });
}
@tucq88
tucq88 commented on Nov 12
So the SASS changes you gonna reload the browser instead of inject only changes ?
@dickmancharles
 Styling with Markdown is supported
Write Preview

Leave a comment
Attach files by dragging & dropping,  Choose Files selecting them, or pasting from the clipboard.
Comment
Status API Training Shop Blog About Pricing
© 2015 GitHub, Inc. Terms Privacy Security Contact Help