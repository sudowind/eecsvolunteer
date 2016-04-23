var rows = {};

function apply_case(id) {
    $.ajax({
        "url": "apply/?id=" + id,
        "type": "GET",
        "dataType": "json",
        "async": false,
        "success": function (data) {
            if (data['code'] == 1) {
                tips('申请成功', 'success');
                maintaining(id);
            }
            else if (data['code'] == 2) {
                confirm_maintain(id);
            }
            else {
                var msg = data['msg'] || '申请失败';
                tips(msg, 'error');
            }
            load_case_table();
        },
        "error": function () {
            tips('连接超时', 'error');
        }
    });
}

function success_case(id) {
    var solution = $('#solution').val();
    var volunteer = $('#volunteer').val();
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        'url': 'success/',
        'type': 'POST',
        'data': {
            csrfmiddlewaretoken: csrftoken,
            id: id,
            solution: solution,
            volunteer: volunteer
        },
        "dataType": "json",
        "async": false,
        "success": function (data) {
            if (data['code'] == 1) {
                tips('记录成功', 'success');
            } else {
                var msg = data['msg'] || '记录失败';
                tips(msg, 'error');
                fail_case(id, true);
            }
            load_case_table();
        },
        "error": function () {
            tips('连接超时', 'error');
        }
    });
}

function fail_case(id, notips) {
    console.log(rows[id]);
    if (rows[id]['status'] == 3)
        return;
    $.ajax({
        "url": "fail/?id=" + id,
        "type": "GET",
        "dataType": "json",
        "async": false,
        "success": function (data) {
            if (data['code'] == 1) {
                if (!notips)
                    tips('记录成功', 'success');
            } else {
                var msg = data['msg'] || '记录失败';
                tips(msg, 'error');
            }
            load_case_table();
        },
        "error": function () {
            tips('连接超时', 'error');
        }
    });
}

function confirm_maintain(id) {
    $('#maintainBtn').attr('onclick', 'maintaining('+id+')');
    $('#maintainModal').modal('show');
}
function maintaining(id) {
    var fields = ['owner', 'computer_model', 'problem', 'solution', 'volunteer'];
    for (var f in fields) {
        $('#'+fields[f]).text(rows[id][fields[f]]);
        $('#'+fields[f]).val(rows[id][fields[f]]);
    }
    $('#failBtn').attr('onclick', 'fail_case('+id+')');
    $('#successBtn').attr('onclick', 'success_case('+id+')');
    //$('#maintainingModal').on('hide.bs.modal', function () {
    //   fail_case(id, true);
    //});
    $('#maintainingModal').modal('show');
}

function load_case_table() {
    rows = {};
    var aid = $('#activity').val();
    var url = '../case_history/get_case_table/?aid='+aid;
    $('#case_table').bootstrapTable('destroy');
    $('#case_table').bootstrapTable({
        url: url,
        method: 'get',
        classes: 'table table-condensed table-hover table-striped',
        dataType: 'json',
        pagination: true,
        pageSize: 10,
        showRefresh: true,
        search: true
    });
}

function id_formatter(value, row) {
    rows[value] = row;
    return '<button class="btn btn-primary" onclick="apply_case('+value+')"> 申请维修 </button>';
}

function status_formatter(value, row) {
    var ret = '';
    switch (value) {
        case 0: ret = 'unknown';break;
        case 1: ret = '<span class="text-danger">待维修</span>';break;
        case 2: ret = '<span class="text-warning">维修中</span>';break;
        case 3: ret = '<span class="text-success">已维修</span>';break;
    }
    return ret;
}

$(document).ready(function(){

    $.ajax({
        "url": "../activity/get_activity_table/",
        "type": "GET",
        "dataType": "json",
        "async": false,
        "success": function (data) {
            load_activity_select(data);
        },
        "error": function () {
            tips('连接超时', 'error');
        }
    });
});

function load_activity_select(data) {
    var select = document.getElementById('activity');
    var now = 0;
    for (var d in data) {
        select.options.add(new Option(data[d]['date'], data[d]['id']));
        now = Math.max(now, data[d]['id']);
    }
    $('#activity').val(now);
    load_case_table();
}