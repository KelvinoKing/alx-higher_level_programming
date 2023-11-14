#!/usr/bin/node
function callMeMoby (x, theFunction) {
  if (x > 0) {
    theFunction();
    exports.callMeMoby(x - 1, theFunction);
  }
}

module.exports = {
  callMeMoby
};
