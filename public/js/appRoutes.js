// public/js/appRoutes.js
    angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

    $routeProvider

        // home page
        .when('/', {
            templateUrl: 'views/home.html',
            controller: 'HomeController'
        })


		// nerds page that will use the NerdController
        .when('/player', {
            templateUrl: 'views/player.html',
            controller: 'PlayerController'
        })
        .otherwise(
          {redirectTo : '/'}
        )

    $locationProvider.html5Mode({
      enabled: true,
      requireBase: true
    });

}]);
