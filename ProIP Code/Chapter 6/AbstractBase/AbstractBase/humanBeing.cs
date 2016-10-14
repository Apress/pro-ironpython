using System;

abstract class humanBeing
{
    public string name { get; private set; }
    public DateTime? dateOfBirth { get; private set; }

    public void SetName(string _name)
    {
        if (String.IsNullOrEmpty(_name)) { throw new Exception("Name cannot be null."); }
        name = _name;
    }

    public void SetDateOfBirth(DateTime? _dateOfBirth)
    {
        if (!_dateOfBirth.HasValue) { throw new Exception("Date of birth cannot be null."); }
        dateOfBirth = _dateOfBirth;
    }

    public abstract void Initialize();
    public abstract void CleanUp();
    public new abstract string ToString();
}
