var app = angular.module('bookApp', []);

app.controller('BooksController', function ($scope, $http) {
    $scope.books = [];

    $scope.getBooks = function () {
        $http.get('/api/books').then(function (response) {
            $scope.books = response.data;
        });
    };

    $scope.addBook = function () {
        $http.post('/api/books', $scope.bookData).then(function (response) {
            $scope.getBooks();
            $scope.resetBookData();
        });
    };

    $scope.updateBook = function (bookId) {
        $http.put('/api/books/' + bookId, $scope.bookData).then(function (response) {
            $scope.getBooks();
            $scope.resetBookData();
        });
    };

    $scope.deleteBook = function (bookId) {
        $http.delete('/api/books/' + bookId).then(function (response) {
            $scope.getBooks();
        });
    };

    $scope.editBook = function (bookId) {
        $http.get('/api/books/' + bookId).then(function (response) {
            $scope.bookData = response.data;
        });
    };

    $scope.saveBook = function () {
        if ($scope.bookData.id) {
            // Update existing book
            $scope.updateBook($scope.bookData.id);
        } else {
            // Add new book
            $scope.addBook();
        }
    };
    
    $scope.resetBookData = function () {
        $scope.bookData = {
            title: '',
            author: '',
            year: ''
        };
    };

    $scope.resetBookData();
    $scope.getBooks();
});
