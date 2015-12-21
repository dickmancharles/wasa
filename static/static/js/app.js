// myModule.config(function($interpolateProvider) {
// 	$httpProvider.defualts.xsrfCookieName = 'csrftoken';
// 	$httpProvider.defualts.xsrfHeaderName = 'X-CSRFToken';
// });


(function(){
	var app = angular.module('wasa', []);

	app.controller('TabController', function(){
    	
    	this.tab = 1;
	    
	    this.setTab = function(setTab){
	      this.tab = setTab; 
	    };
	    
	    this.isSet = function(isSet){
        	return this.tab === isSet;
    	};
    });

	app.controller('CareerController', function(){
    	
    	this.tab = 1;
	    
	    this.setTab = function(setTab){
	      this.tab = setTab; 
	    };
	    
	    this.isSet = function(isSet){
        	return this.tab === isSet;
    	};
    });

	app.controller('LocationController', function(){
    	
    	this.tab = 1;
	    
	    this.setTab = function(setTab){
	      this.tab = setTab; 
	    };
	    
	    this.isSet = function(isSet){
        	return this.tab === isSet;
    	};
    });

	app.config(function($interpolateProvider) {
		$interpolateProvider.startSymbol('[[').endSymbol(']]');
		
	});

})();