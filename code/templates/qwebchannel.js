/*!
 * Qt WebChannel qwebchannel.js
 *
 * Copyright (c) 2013 Digia Plc and/or its subsidiary(-ies).
 * SPDX-License-Identifier: LGPL-3.0-only OR LGPL-2.1-only OR GPL-2.0-only OR GPL-3.0-only
 */

(function(global) {
    "use strict";

    function throwError(msg) {
        if (typeof console !== "undefined" && console.error) {
            console.error(msg);
        }
        throw msg;
    }

    function isFunction(func) {
        return typeof func === "function";
    }

    function WebChannel(transport, initCallback) {
        var channel = this;
        this.transport = transport;
        this.objects = {};
        this.exec = function(data) {
            if (data.id !== undefined) {
                if (isFunction(channel.callbacks[data.id])) {
                    channel.callbacks[data.id](data.data);
                    delete channel.callbacks[data.id];
                }
            } else if (data.signal !== undefined) {
                if (channel.objects[data.object]) {
                    channel.objects[data.object].signalEmitted(data.signal, data.args);
                }
            } else if (data.property !== undefined) {
                if (channel.objects[data.object]) {
                    channel.objects[data.object].propertyChanged(data.property, data.value);
                }
            }
        };
        this.callbacks = {};
        this.debug = false;
        this.send = function(data) {
            if (channel.debug) {
                console.log("sending", data);
            }
            channel.transport.send(JSON.stringify(data));
        };
        this.transport.onmessage = function(message) {
            if (channel.debug) {
                console.log("received", message.data);
            }
            channel.exec(JSON.parse(message.data));
        };
        this.sendInitMessage = function() {
            this.send({type: "init"});
        };
        this.transport.onopen = function() {
            channel.sendInitMessage();
        };
        if (isFunction(initCallback)) {
            this.onInit = initCallback;
        }
    }

    global.QWebChannel = WebChannel;

})(this);
