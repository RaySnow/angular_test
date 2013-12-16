var ifControllers = angular.module('ifControllers', []);
 ifControllers.controller('Ctrl', function($scope) {
        $scope.info = "";
        $scope.customer = {
          name: 'Naomi',
          address: '1600 Amphitheatre'
        };
  });
ifControllers.directive('myCustomer', function() {
    function link(scope, element, attrs) {
        element.on('click',function(){
            if (scope.info) {
                var phone = '';
                var email = '';
                if (scope.info.match(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]+$/)) {
                     email = scope.info;
                }
                if(scope.info.match(/^1[3|4|5|8][0-9]\d{4,8}$/)){
                      phone = scope.info;
                }
                if(email || phone){
                    $http({
                        method: 'POST',
                        url: "/info",
                        params: {
                            'email': email,
                            'phone': phone
                        },
                        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                    }).success(function () {
                            alert("感谢您的支持，我们会第一时间告知您。");
                        })
                }
                else {
                    alert("请输入正确的邮箱或手机号");
                    element.parent().prev().children("input").focus().select();
                }
            }
            else {
                alert("请填写您的邮箱或手机号，谢谢您的支持");
            }
      });
    }
    return {
        link: link
    };
  });