package com.example.api.users;

import org.springframework.data.repository.CrudRepository;

interface UserRepository extends CrudRepository<User, Integer> {
}
