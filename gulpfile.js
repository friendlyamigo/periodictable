'use strict';
var gulp = require('gulp'),
    sass = require('gulp-ruby-sass'),
    browsersync = require('browser-sync'),
    shell = require('gulp-shell'),
    jade = require('gulp-jade');

gulp.task('sass', function(){
  return sass('src/sass/main.sass')
  .on('error', sass.logError)
  .pipe(gulp.dest('dest'));
});

gulp.task('jade', function(){
  gulp.src('src/jade/index.jade')
  .pipe(jade({pretty: true}))
  .pipe(gulp.dest('dest'));
});

gulp.task('browsersync', function(){
  browsersync.init({
    server: {
      baseDir: './dest'
    }
  });
});

gulp.task('js', function(){
  gulp.src('src/*.js')
  .pipe(gulp.dest('dest'));
});

gulp.task('scrape', shell.task([
  'python resources/scraper.py'
]));

gulp.task('default', ['sass','js', 'jade', 'browsersync'],function(){
  gulp.watch('src/sass/**/*.*', ['sass']);
  gulp.watch('src/jade/**/*.*', ['jade']);
  gulp.watch('src/*.js', ['js']);
  gulp.watch('dest/*.*').on('change', browsersync.reload);
});
