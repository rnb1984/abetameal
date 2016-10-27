
var mealApp = angular.module('mealApp',[])
    .config(['$httpProvider', function($httpProvider) {
        // set CSRF for Django
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);



// Controller for pizzas
mealApp.controller('mealController', function ($scope, $http, $rootScope ) {

    // urls
    var meal_in = $http.get("api/meals/"),
    ingredients_in = $http.get("api/ingredients/"),
    pairs_in = $http.get('/api/u/pairs/first/'),
    users_in = $http.get('/api/users/'),
    dinner_in = $http.get('/api/dinners/'),
    homes_in = $http.get('/api/homes/');
    
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
       pairs_in.then(function (response) {
        $scope.pairs = response.data
      });
    users_in.then(function (response) {
        // set paramaters
        $scope.users = response.data
      });
    dinner_in.then(function (response) {
        // set paramaters
        $scope.dinners = response.data
      });
     homes_in.then(function (response) {
        // set paramaters
        $scope.homes = response.data
      });
      
    
     // remove
     $scope.remove = function(){
     };
     
     // add
     $scope.add = function(){
     };
     
});

