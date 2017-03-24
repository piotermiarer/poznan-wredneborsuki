const gulp = require('gulp');
const sass = require('gulp-sass');
const concat = require('gulp-concat');

const srcs = {
    'styles': `${__dirname}/scss/**/*.scss`,
    'javascript': `${__dirname}/js/**/*.js`,
    'images': `${__dirname}/images/**/*.svg`
};

const dests = {
    'styles': `${__dirname}/../ballegro/static/css`,
    'javascript': `${__dirname}/../ballegro/static/js`,
    'images': `${__dirname}/../ballegro/static/images`
};

gulp.task('sass', () => {
    return gulp.src(srcs['styles']).pipe(sass().on('error', sass.logError)).pipe(gulp.dest(dests['styles']));
});

gulp.task('sass:watch', () => {
    gulp.watch(srcs['styles'], ['sass']);
});

gulp.task('javascript', () => {
    return gulp.src(srcs['javascript']).pipe(gulp.dest(dests['javascript']));
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

gulp.task('build:watch', ['sass:watch', 'images:watch', 'javascript:watch'], () => {
    return true;
});
