// public/js/controllers/PlayerCtrl.js


angular.module('PlayerCtrl', []).controller('PlayerController', ['$scope','$routeParams','Upload','$q', 'Player','Auth', function($scope, $routeParams, Upload, $q, Player, Auth) {

	//Auth.getUser(function(user){$scope.currentUser = user;});
	$scope.customize = false;
	$scope.rand = Math.random();
	$scope.playercolor = '#ffffff';

	$scope.showError = function (error) {
        notifications.showError({
            message: error,
            hideDelay: 2000, //ms
            hide: true //bool
        });
    };


		////console.log(sessionData);

	// upload on file select or drop
    $scope.upload = function (file) {
        Upload.upload({
            url: '/upload',
            data: {file: file, 'playerid': $scope.player.playerid, 'playercolor':$scope.playercolor}
        }).then(function (resp) {
            console.log('Success ' + resp.config.data.file.name + 'uploaded. Response: ' + resp.data);
			$scope.rand = Math.random();
        }, function (resp) {
            console.log('Error status: ' + resp.status +": "+ resp.data);
			$scope.showError(resp.data);
        }, function (evt) {
            var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
            console.log('progress: ' + progressPercentage + '% ' + evt.config.data.file.name);
        }

		);
    };

	$scope.$watch('rand',function(){
		//console.log("rules changed");
	});
	$scope.$watch('file',function(){
		//console.log("rules changed");
	});
	$scope.$watch('playercolor',function(){
		//console.log($scope.playercolor);
	});


}]);
