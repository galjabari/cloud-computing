angular.module('bookApp', []);

angular.module('bookApp').controller('bookController', function($scope, bookService) {
  // Fetch all books from the server
  bookService.getBooks().then(function(response) {
    $scope.books = response.data;
  });

  // Add a new book
  $scope.addBook = function() {
    bookService.addBook($scope.newBook).then(function(response) {
      $scope.books.push(response.data);
      $scope.newBook = {}; // Clear the input fields
    });
  };

  // Delete a book
  $scope.deleteBook = function(book) {
    bookService.deleteBook(book._id).then(function(response) {
      console.log(response.data.message);
      // Remove the deleted book from the array
      var index = $scope.books.indexOf(book);
      if (index > -1) {
        $scope.books.splice(index, 1);
      }
    });
  };
});

angular.module('bookApp').factory('bookService', function($http) {
  return {
    getBooks: function() {
      return $http.get('/api/books');
    },
    addBook: function(book) {
      return $http.post('/api/books', book);
    },
    deleteBook: function(bookId) {
      return $http.delete('/api/books/' + bookId);
    }
  };
});
