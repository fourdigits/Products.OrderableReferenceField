/*jslint browser: true */
/*global window, jQuery */


var referencebrowser_openBrowser,
    referencebrowser_setReference,
    referencebrowser_removeReference,
    referencebrowser_updateIndexItems;


jQuery(function($) {

"use strict";


referencebrowser_updateIndexItems = function(id) {
    var $lis = $('#'+id+' li');

    $lis.each(function(li_idx, li) {
        $('.orderablereferencebrowser_arrow', li).each(function(updn_idx, a) {
            var handler = null;
            if (updn_idx === 0 && li_idx > 0) {
                handler = function(ev) {
                    $($lis[li_idx]).insertBefore($lis[li_idx-1]);   // moveup
                    ev.preventDefault();
                    referencebrowser_updateIndexItems(id);
                };
            } else if (updn_idx === 1 && li_idx < $lis.length - 1) {
                handler = function(ev) {
                    $($lis[li_idx]).insertAfter($lis[li_idx+1]);    // movedown
                    ev.preventDefault();
                    referencebrowser_updateIndexItems(id);
                };
            }

            $(a).unbind('click').css({'cursor': 'auto', visibility: 'hidden'});
            if (handler) {
                $(a).click(handler).css({'cursor': 'pointer', 'color': '', visibility: 'visible'});
            }
        });
    });
};



// function to open the popup window
referencebrowser_openBrowser = function(path, fieldName, at_url, fieldRealName) {
    window.open(path + '/referencebrowser_popup?fieldName=' + fieldName + '&fieldRealName=' + fieldRealName +'&at_url=' + at_url,
                'referencebrowser_popup',
                'toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=500,height=550');
};


// function to return a reference from the popup window back into the widget
referencebrowser_setReference = function(widget_id, uid, label, multi) {
    var $input;
    // differentiate between the single and mulitselect widget
    // since the single widget has an extra label field.
    if (multi === 0) {
        $('#'+widget_id).val(uid);
        $('#'+widget_id+'_label').val(label);
     } else {
        // check if the item isn't already in the list
        $('#'+widget_id+' input').each(function() {
            if ($(this).val() === uid) {
                return false;
            }
        });

        $input = $('<input type="checkbox" checked="true" />').val(uid).attr('name', widget_id+':list');

        $('<li></li>').append(
            $('<a class="orderablereferencebrowser_arrow">&#x25B2;</a>'), document.createTextNode(' '),
            $('<a class="orderablereferencebrowser_arrow">&#x25BC;</a>'), document.createTextNode(' '),
            $('<label></label>').append($input, document.createTextNode(' '+label))
        ).appendTo('#'+widget_id);

        $input.attr('checked', 'true');         // fix on IE7 - check *after* adding to DOM
        referencebrowser_updateIndexItems(widget_id);
    }
};


// function to clear the reference field or remove items
// from the multivalued reference list.
referencebrowser_removeReference = function(widget_id, multi) {
    var x, list;
    if (multi === 0) {
        $('#'+widget_id).val('');
        $('#'+widget_id+'_label').val('');
    } else {
        list = document.getElementById(widget_id);
        for (x = list.length-1; x >= 0; x--) {
            if (list[x].selected) {
                list[x] = null;
            }
        }
        for (x = 0; x < list.length; x++) {
            list[x].selected = 'selected';
        }
    }
};

});
