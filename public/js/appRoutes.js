// public/js/appRoutes.js
    angular.module('appRoutes', []).config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

    $routeProvider

        // home page
        .when('/', {
            templateUrl: 'views/home.html',
            controller: 'HomeController'
        })

        .when('/signatures/', {
            templateUrl: 'views/home.html',
            controller: 'HomeController'
        })

        .otherwise(
          {
            redirectTo : '/signatures/'
          }
        )

    $locationProvider.html5Mode({
      enabled: true,
      requireBase: true/// HACK: Offline mode
    });

}]);
