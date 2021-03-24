#!/usr/bin/node

exports.converter = function (base) {
    return integer => integer.toString(base);
};