// public/js/controllers/MainCtrl.js


angular.module('MainCtrl', []).controller('MainController', ['$scope','Auth','$window','$document', function($scope, Auth, $window,$document) {

	Auth.getUser(function(user){
		$scope.currentUser = user;
	});

	$scope.$watch('currentUser',function(){
		//console.log("user changed");
	});

}]);
