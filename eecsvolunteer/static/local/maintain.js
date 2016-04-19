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

}

function create_activity() {
    var date = $('#activity_date').val();
    var place = $('#activity_place').val();
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        'url': 'maintain/',
        'type': 'post',
        'data': {
            csrfmiddlewaretoken: csrftoken,
            date: date,
            place: place
        },
        'dataType': 'json',
        "async": false,
        'success': function(data) {
            if (data['code'] == 1) {
                tips('添加成功', 'success');
                load_activity_table()
            }
            else {
                var msg = data['msg'] || '添加失败';
                tips(msg, 'error');
            }
        },
        "error": function () {
            tips('连接超时', 'error');
        }
    });
}

function load_case_table(aid) {
    aid = 1;
    var url = '../case_history/get_case_table/?aid='+aid;
    $('#case_table').bootstrapTable('destroy');
    $('#case_table').bootstrapTable({
        url: url,
        method: 'get',

        classes: 'table table-condensed table-hover table-striped',
        dataType: 'json',
        pagination: true,
        pageSize: 10
    });
}

function id_formatter(value, row) {
    return '<button class="btn btn-primary" onclick="apply_case('+value+')"> 申请维修 </button>'
}

function status_formatter(value, row) {
    var ret = '';
    switch (value) {
        case 0: ret = 'unknown';break;
        case 1: ret = '待维修';break;
        case 2: ret = '维修中';break;
        case 3: ret = '已维修';break;
    }
    return ret;
}
