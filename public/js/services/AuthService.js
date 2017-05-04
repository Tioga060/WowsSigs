// public/js/services/AuthService.js
angular.module('AuthService', []).service('Auth',['$http','$q', function($http,$q) {
	var me = this;

	function getUser(callback) {
		// if the user has already been retrieved then do not do it again, just return the retrieved instance
		if(me.currentUser )
			callback(me.currentUser);
		// retrieve the currentUser and set it as a property on the service
		else {
			$http.get('/signatures/api/cookie/?format=json').then(function(res){
			  // set the result to a field on the service
        //console.log(res.data)
			  if(res.data[0].username){
				  me.currentUser = res.data[0];
				  // call the callback with the retrieved user
				  //console.log("found him");
				  //console.log(res.data);
				  me.currentUser["profile"] = "/signatures/";
				  me.currentUser["loggedin"] = true;
				  callback(me.currentUser);
			  }
			  else{
				  callback({'username': "Log in", 'profile':'/openid/login', 'loggedin': false});
			  }
			});
		}

	}
  return {getUser:getUser}
}]);
