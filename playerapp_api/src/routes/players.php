<?php
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

$app = new \Slim\App(['settings' => ['displayErrorDetails' => true]]);

# Get All Players
$app->get('/api/players', function(Request $request, Response $response){
    //echo 'PLAYERS';
    $sql = "SELECT * FROM players";

    try{
        //get db object
        $db = new db();
        //Connect
        $db = $db->connect();

        $stmt = $db->query($sql);
        $players = $stmt->fetchAll(PDO::FETCH_OBJ);
        
        $db = null;
        echo json_encode($players);
      // echo 'connected';
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
     
});

# Get Single Player
$app->get('/api/player/{id}', function(Request $request, Response $response){
    $id = $request->getAttribute('id');
    
    $sql = "SELECT * FROM players WHERE id = $id";

    try{
        //get db object
        $db = new db();
        //Connect
        $db = $db->connect();

        $stmt = $db->query($sql);
        $player = $stmt->fetchAll(PDO::FETCH_OBJ);
        
        $db = null;
        echo json_encode($player);
      // echo 'connected';
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
     
});


# Get specific team and season
$app->get('/api/{team}/{season}', function(Request $request, Response $response){
    $season = $request->getAttribute('season');
    $team = $request->getAttribute('team');
    $sql = "SELECT * FROM players WHERE season = $season AND team = '$team'";
    echo $sql;

    try{
        //get db object
        $db = new db();
        //Connect
        $db = $db->connect();

        $stmt = $db->query($sql);
        $player = $stmt->fetchAll(PDO::FETCH_OBJ);
        
        $db = null;
        echo json_encode($player);
      // echo 'connected';
    } catch(PDOException $e){
        echo '{"error": {"text": '.$e->getMessage().'}';
    }
     
});
