public interface IUserRepository
{
    Task<IEnumerable<User>> GetAll();
    Task<bool> Create(User user);
}