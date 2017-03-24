const fs = require('fs');
const gulp = require('gulp');
const sass = require('gulp-sass');
const concat = require('gulp-concat');
const watchify = require('watchify');
const browserify = require('browserify');
const source = require('vinyl-source-stream');
const buffer = require('vinyl-buffer');
const sourcemaps = require('gulp-sourcemaps');

const srcs = {
    'styles': `${__dirname}/scss/**/*.scss`,
    'javascript': [
        `${__dirname}/js/main.js`,
    ],
    'images': `${__dirname}/images/**/*.svg`
};

const dests = {
    'styles': `${__dirname}/../ballegro/static/css`,
    'javascript': `${__dirname}/../ballegro/static/js/`,
    'images': `${__dirname}/../ballegro/static/images`
};

gulp.task('sass', () => {
    return gulp.src(srcs['styles'])
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(dests['styles']));
});

gulp.task('sass:watch', () => {
    gulp.watch(srcs['styles'], ['sass']);
});

gulp.task('javascript', () => {
    return browserify({
        entries: srcs['javascript'],
        debug: true
    })
        .bundle()
        .pipe(source('bundle.js'))
        .pipe(buffer())
        .pipe(sourcemaps.init({
            loadMaps: true
        }))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(dests['javascript']));
});

gulp.task('javascript:watch', () => {
    gulp.watch(srcs['javascript'], ['javascript']);
});

gulp.task('images', () => {
    return gulp.src(srcs['images']).pipe(gulp.dest(dests['images']));
});

gulp.task('images:watch', () => {
    gulp.watch(srcs['images'], ['images']);
});

gulp.task('build', ['sass', 'images', 'javascript'], () => {
    return true;
});

gulp.task('build:watch', ['sass:watch', 'images:watch', 'javascript'], () => {
    return true;
});
