public interface IUserRepository
{
    Task<IEnumerable<User>> GetAll();
    Task<User> Create(User user);
}