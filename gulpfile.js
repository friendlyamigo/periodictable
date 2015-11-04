'use strict';
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    browsersync = require('browser-sync'),
    jade = require('gulp-jade');

gulp.task('sass', function(){
  gulp.src('src/sass/main.sass')
  .pipe(sass())
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

gulp.task('server', ['sass','js', 'jade', 'browsersync'],function(){
  gulp.watch('src/sass/*.*', ['sass']);
  gulp.watch('src/jade/*.*', ['jade']);
  gulp.watch('src/*.js', ['js']);
  gulp.watch('dest/*.*').on('change', browsersync.reload);
});

gulp.task('default', function(){

});
