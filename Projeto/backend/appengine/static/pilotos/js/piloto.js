/**
 * Created by Anderson on 05/11/2014.
 */

var pilotoModulo = angular.module('pilotoModulo',[]);


pilotoModulo.directive('pilotosForm',function(){
    return{
        restrict:'E',
        replace:true,
        templateUrl:'/static/pilotos/html/piloto_form.html'
    };
});
