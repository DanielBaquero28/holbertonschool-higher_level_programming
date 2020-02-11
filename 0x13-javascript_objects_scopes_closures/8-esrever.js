#!/usr/bin/node
exports.esrever = function (list) {
  const listRev = [];
  for (let i = list.length - 1; i < list.length; i--) {
    listRev.push(list[i]);
  }
  return (listRev);
};
