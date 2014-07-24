(function() {
  var tr = $('table#artists tbody tr');
  var artistIds = [];
  for(i=0; i <= tr.length; i++) {
    var id = $(tr[i]).data('artist-id');
    if(id !== undefined) {
      artistIds.push(id);
    }
  }

  $.ajax({
    'url': window.dvRoute['user.is_love_artist'],
    'data': 'artist_ids=' + artistIds.join(','),
    'type': 'GET',
    'success': function(data) {
      console.log(data);
      if(data !== undefined) {
        console.log(data['artist_ids'])
        for(i=0; i <= tr.length; i++) {
          var mytr = $(tr[i]);
          var id = mytr.data('artist-id');
          console.log('a', typeof(id), id);
          console.log('b', typeof(data['artist_ids'][0]), data['artist_ids']);
          console.log(id in data['artist_ids'])
          if(data.hasOwnProperty('artist_ids')
            && data['artist_ids'].indexOf(id) != -1) {
            mytr.find('td > form > button').addClass('loved')
          }
        }
      }
    }
  });
})();
