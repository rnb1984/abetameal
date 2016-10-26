
var mealApp = angular.module('mealApp',[])
    .config(['$httpProvider', function($httpProvider) {
        // set CSRF for Django
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);



// Controller for pizzas
mealApp.controller('mealController', function ($scope, $http, $rootScope ) {

    // urls
    var meal_in = $http.get("api/meals/"), ingredients_in = $http.get("api/ingredients/");
    
    // vars
    $scope.master={};
    
    meal_in.then(function (response) {
        // set paramaters
        $scope.meals = response.data
      });
    ingredients_in.then(function (response) {
        // set paramaters
        $scope.ingredients = response.data
      });
      
    
     // remove
     $scope.remove = function(){
     };
     
     // add
     $scope.add = function(){
     };
     
});

