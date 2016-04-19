/**
 * Created by Wind on 2016/4/19.
 */
function add_case() {
    var owner = $('#owner').val();
    var contact = $('#contact').val();
    var model = $('#computer_model').val();
    var problem = $('#problem').val();
    if (owner == '' || model == '' || problem == '') {
        tips('请填写缺失项', 'info');
        return;
    }
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: 'add_case/',
        method: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: csrftoken,
            owner: owner,
            contact: contact,
            model: model,
            problem: problem
        },
        async: false,
        success: function(data) {
            if (data['code'] == 1) {
                tips('添加成功', 'success');
                var wait_count = data['wait_count'];
                $('#info_message').html(
                    '<span style="color: green">还需等待' + wait_count.toString() + '人</span>'
                );
            }
            else {
                var msg = data['msg'] || '添加失败';
                tips(msg, 'error');
            }
        },
        error: function() {
            tips('连接超时', 'error');
        }
    });
}