const SVGInjector = require('svg-injector');

module.exports = function teamShow() {
    injectSVGs({});
}

function injectSVGs(opts) {
    const toInject = Function.prototype.slice.call(document.querySelectorAll('img.svg-injection'), 0);
    return new Promise((resolve, reject) => {
        SVGInjector(toInject, opts, count => {
            if (count != toInject.length) reject('Some elements hasn\'t been inserted');
            else resolve();
        });
    });
}
