#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const listO = [];
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      listO.append(list[i])
    }
  }
  return (listO.length);
}
