var app = angular.module('bookApp', []);

app.controller('BookController', function ($scope, $http) {
    $scope.books = [];

    // Get all books
    $http.get('/books').then(function (response) {
        $scope.books = response.data;
    });

    // Save a book
    $scope.saveBook = function () {
        if ($scope.newBook.id) {
            // Update existing book
            $http.put('/books/' + $scope.newBook.id, $scope.newBook).then(function () {
                $scope.clearForm();
                refreshBooks();
            });
        } else {
            // Add new book
            $http.post('/books', $scope.newBook).then(function () {
                $scope.clearForm();
                refreshBooks();
            });
        }
    };

    // Edit a book
    $scope.editBook = function (book) {
        $scope.newBook = angular.copy(book);
    };

    // Delete a book
    $scope.deleteBook = function (id) {
        $http.delete('/books/' + id).then(function () {
            refreshBooks();
        });
    };

    // Clear the form
    $scope.clearForm = function () {
        $scope.newBook = {};
    };

    // Helper function to refresh the list of books
    function refreshBooks() {
        $http.get('/books').then(function (response) {
            $scope.books = response.data;
        });
    }
});
