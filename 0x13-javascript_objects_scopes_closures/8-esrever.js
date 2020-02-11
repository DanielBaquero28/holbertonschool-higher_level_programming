#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    listRev[i] = list[j];
  }
  return (listRev);
};
