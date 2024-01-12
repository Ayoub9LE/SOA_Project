package com.example.CrudAppl.Controller;

import com.example.CrudAppl.Entity.User;
import com.example.CrudAppl.Service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping
    public List<User> findAllUsers() {
        return userService.findAllUsers();
    }

    @PostMapping("/add")
    public User insertUser(@RequestBody User user) {
        return userService.insertUser(user);
    }

    @GetMapping("/{id}")
    public Optional<User> findUserById(@PathVariable Long id) {
        return userService.findUserById(id);
    }

    @PutMapping("/update/{id}")
    public User updateUser(@PathVariable("id") Integer userId, @RequestBody User user) {
        // Set the user ID from the path variable to the User object
        user.setId(userId);
        // Call the service to update the user
        return userService.updateUser(user);
    }


    @DeleteMapping("delete/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
