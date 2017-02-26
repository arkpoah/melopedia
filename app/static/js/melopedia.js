$( document ).ready(function() {

$("#fychk").click(function(){
   if ($("#art_drop").is(":visible")) {
         $("#art_drop").hide();
         $("#alb_drop").show();
      } else {
        $("#alb_drop").hide();
        $("#art_drop").show();
      }
});

$("#art_drop .dropdown-menu li a").click(function() {
  window.location.href = '/artists/year/' + $(this).html()
});
$("#alb_drop .dropdown-menu li a").click(function() {
  window.location.href = '/albums/year/' + $(this).html()
});


$.typeahead({
    input: '.js-typeahead-game_v1',
    minLength: 1,
    maxItem: 0,
    maxItemPerGroup: 16,
    order: "asc",
    hint: true,
    group: true,
    maxItemPerGroup: 5,
    dropdownFilter: "all",
    source: {
        Artist: {
          ajax: {
                url: "/_all.json",
                dataType: "json",
                path: "data.artists"
            }
        },
        Album: {
            ajax: {
                url: "/_all.json",
                dataType: "json",
                path: "data.albums"
            }
        },
        Tag: {
            ajax: {
                url: "/_all.json",
                dataType: "json",
                path: "data.tags"
            }
        }
    },
    callback: {
        onNavigateBefore: function (node, query, event) {
            if (~[38,40].indexOf(event.keyCode)) {
                event.preventInputChange = true;
            }
        },
        onClick: function (node, a, item, event) {
          if (item.group !== "Album") {
            window.open(
                    item.group.toLowerCase() + "/" +
                    item.slug
            ,"_self");
          }
          else {
            window.open(
              item.group.toLowerCase() + "/" + item.id
              ,"_self");
            }
        },
        onMouseEnter: function (node, a, item, event) {
            if (item.group !== "Artist") {
                return false;
            }
 
            if (!$(a).find(".popover")[0]) {
 
                $(a).append(
                    $("<div/>", {
                        "class": "popover fade right in",
                        "html": $("<div/>", {
                            "class": "popover-content",
                            "html": $("<img/>", {
                                "src": item.img
                            })
                        }).prepend($("<div/>", {
                            "class": "arrow"
                        }))
                    })
                );
 
            } else {
                $(a).find(".popover").removeClass("out").addClass("in");
            }
        },
        onMouseLeave: function (node, a, item, event) {
            if (item.group !== "Artist") {
                return false;
            }
 
            $(a).find(".popover").removeClass("in").addClass("out");
        }
    }
});

});

