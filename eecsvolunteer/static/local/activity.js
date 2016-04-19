/**
 * Created by Wind on 2016/4/19.
 */
function confirm_delete(id) {
    $('#deleteBtn').attr('onclick', 'delete_activity('+id+')');
    $('#deleteModal').modal('show');
}

function delete_activity(id) {
    $.ajax({
        "url": "delete/?id=" + id,
        "type": "GET",
        "dataType": "json",
        "async": false,
        "success": function (data) {
            if (data['code'] == 1) {
                tips('删除成功', 'success');
                location.reload();
            } else {
                var msg = data['msg'] || '删除失败';
                tips(msg, 'error');
            }
        },
        "error": function () {
            tips('连接超时', 'error');
        }
    });
}
function create_activity() {
    var date = $('#activity_date').val();
    var place = $('#activity_place').val();
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        'url': 'create/',
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
                location.reload();
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