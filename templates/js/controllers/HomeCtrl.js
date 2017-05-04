// public/js/controllers/HomeCtrl.js


angular.module('HomeCtrl', []).controller('HomeController', ['$scope','$routeParams', 'Auth', function($scope, $routeParams, Auth) {

	$scope.tagline = 'Tioga.moe Rules!';
	//Auth.getUser(function(user){$scope.currentUser = user;});

}]);
