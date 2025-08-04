using Microsoft.EntityFrameworkCore;

public class UserRepository: IUserRepository
{
    private readonly ApplicationDbContext _context;

    public UserRepository(ApplicationDbContext context)
    {
        _context = context;
    }
    public async Task<IEnumerable<User>> GetAll()
    {
        return await _context.Users.AsNoTracking().ToListAsync();
    }

    public async Task<bool> Create(User user)
    {
        _context.Users.Add(user);
        return await _context.SaveChangesAsync() > 0;
    }
}